convert_file='
  input_file="phenos.BT.step2_both_morphine_fentanyl.regenie"
  output_file="phenos.BT.step2_both_morphine_fentanyl.txt"

  # Step 1: Add a header to the output file
  echo -e "CHROM\tGENPOS\tID\tALLELE0\tALLELE1\tA1FREQ\tN\tTEST\tBETA\tSE\tCHISQ\tLOG10P\tEXTRA" > $output_file

  # Step 2: Convert spaces to tabs and append to the output file
  tail -n+2 "$input_file" | tr " " "\t" >> $output_file

  # Notify the user
  echo "Conversion completed: $output_file"
'

dx run swiss-army-knife \
  -iin="/WGS_Lucia/Data/Output_regenie/regenie_single_variant_test/phenos.BT.step2_both_morphine_fentanyl.regenie" \
  -icmd="${convert_file}" \
  --destination="/WGS_Lucia/Data/Output_regenie/regenie_single_variant_test/" \
  --tag="Final" \
  --instance-type "mem1_ssd1_v2_x16" \
  --brief --yes




