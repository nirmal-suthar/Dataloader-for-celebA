### download.sh

downloads the celebA dataset from the drive link as zip file (1.4GB), extracts them and deletes the original zip file
\ngoogle-drive link: https://drive.google.com/drive/folders/0B7EVK8r0v71pWEZsZE9oNnFzTm8

requires

1) requests
2) tqdm

for running script

```bash
   $ chmod +x ./download.sh
   $ ./download.sh celeba
```

### data_loader.py

get_loader function

args

1) image_dir (as specified by download.sh)
2) resize_size (for preprocessing image)
3) batch_size
4) dataset (default: celebA)
4) num_workers (default: 1)

returns

1) data_loader



