import numpy as np
import pandas as pd
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, fcluster


def from_eid_df(eid_df: pd.DataFrame):
    # Sort by start date
    eid_df = eid_df.sort_values("drug_era_start_date").reset_index(drop=True)

    # Initialize sequence
    sequence = []
    for index, row in eid_df.iterrows():
        next_start_date = (
            eid_df["drug_era_start_date"].iloc[index + 1]  # type: ignore
            if index != len(eid_df) - 1
            else pd.NaT
        )
        sequence.append(row["atc_code_num"])
        if (
            index != 0
            and index != len(eid_df) - 1
            and next_start_date - row["drug_era_end_date"] > pd.Timedelta(days=60)
        ):
            sequence.append(0)
    return sequence


def similarity_score(seq1: list, seq2: list) -> int:
    """
    Calculate similarity score between two sequences based on their treatment periods.
    Each unique ending drug is only counted once.

    Scoring rules:
    - Same ending drug in a period: +3 points (counted once per unique ending)
    - Same drug before the ending: +1 point

    Args:
        seq1: First sequence of numbers
        seq2: Second sequence of numbers

    Returns:
        int: Similarity score
    """
    # Split sequences by 0 to get treatment periods
    periods1 = [period for period in "".join(map(str, seq1)).split("0") if period]
    periods2 = [period for period in "".join(map(str, seq2)).split("0") if period]

    total_score = 0
    counted_endings = set()  # Keep track of endings we've already counted

    # Compare each period from seq1 with each period from seq2
    for p1 in periods1:
        for p2 in periods2:
            # Convert back to integers
            p1_nums = [int(x) for x in p1]
            p2_nums = [int(x) for x in p2]

            # Check ending drugs (3 points)
            if p1_nums[-1] == p2_nums[-1]:
                # Only count this ending if we haven't seen it before
                if p1_nums[-1] not in counted_endings:
                    total_score += 3
                    counted_endings.add(p1_nums[-1])

                # Check drugs before ending
                min_len = min(len(p1_nums), len(p2_nums))
                if min_len > 1:
                    # Compare all positions before the last one
                    for i in range(min_len - 1):
                        if p1_nums[i] == p2_nums[i]:
                            total_score += 1

    return total_score


def create_distance_matrix(sequences: list) -> np.ndarray:
    """
    Create a distance matrix using similarity scores between all pairs of sequences.
    Converts similarity scores to distances for clustering.
    """
    n = len(sequences)
    dist_matrix = np.zeros((n, n))

    # First find the maximum possible similarity score to help with normalization
    max_similarity = 0
    for i in range(n):
        for j in range(i + 1, n):
            similarity = similarity_score(sequences[i], sequences[j])
            max_similarity = max(max_similarity, similarity)

    # Create distance matrix where distance = max_similarity - similarity
    for i in range(n):
        for j in range(i + 1, n):
            similarity = similarity_score(sequences[i], sequences[j])
            # Convert similarity to distance: higher similarity = lower distance
            distance = max_similarity - similarity
            dist_matrix[i, j] = distance
            dist_matrix[j, i] = distance

    return dist_matrix


def cluster(sequences: list, n_clusters: int = 5):
    """
    Cluster sequences using hierarchical clustering based on similarity scores

    Args:
        sequences: List of sequences to cluster
        n_clusters: Number of clusters
    """
    # Create distance matrix
    dist_matrix = create_distance_matrix(sequences)

    # Convert to condensed form required by linkage
    condensed_dist = squareform(dist_matrix)

    # Perform hierarchical clustering
    linkage_matrix = linkage(
        condensed_dist, method="average"
    )  # you can try 'single', 'complete', 'ward' etc.

    # Create clusters
    clusters = fcluster(linkage_matrix, n_clusters, criterion="maxclust")

    return clusters, linkage_matrix
