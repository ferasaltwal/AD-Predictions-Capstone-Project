for file in /Users/ferasaltwal/Documents/DSI/New-Capstone/test_images/nii_sorted/CN/*.nii
do
    deepbrain-extractor -i $file -o /Users/ferasaltwal/Documents/DSI/New-Capstone/extraction/brain2/CN-test/${file%.nii}
done
