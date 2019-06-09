from torch.utils import data
from torchvision import transforms
from torchvision.datasets import ImageFolder
import os

class CelebA(data.Dataset):
    """Dataset class for the CelebA dataset."""

    def __init__(self, image_dir, resize_size, transform):
        """Initialize and preprocess the CelebA dataset."""
        self.image_dir = image_dir
        self.attr_path = attr_path
        self.selected_attrs = selected_attrs
        self.resize_size = resize_size
        self.transform = transform
        self.preprocess()


    def preprocess(self):
        """Preprocess the CelebA attribute file."""

            resize_size = self.resize_size
            save_root = 'celeba_processed/'

            if not os.path.isdir(save_root):
                os.mkdir(save_root)
            if not os.path.isdir(save_root + 'celebA'):
                os.mkdir(save_root + 'celebA')

            try:
                img_list = os.listdir(self.image_dir)
            except:
                print('image_dir directory is invalid (if images are present inside folder /celeba/processed/ then specifiy image_dir as /celeba/)')
                return

            for i in range(len(img_list)):
                img = plt.imread(root + img_list[i])
                img = cv2.resize(img, (resize_size,resize_size))
                plt.imsave(fname=save_root + 'celebA/' + img_list[i], arr=img)

                if (i % 1000) == 0:
                    print('%d images complete' % i)
            print('data preprocessing done!')

            dataset = datasets.ImageFolder(data_dir, self.transform)
            return dataset

        print('Finished preprocessing the CelebA dataset...')

    def __getitem__(self, index):
        """Return one image (Yet to inplement)."""
        return None

    def __len__(self):
        """Return the number of images (Yet to implement)."""
        return None


def get_loader(image_dir, resize_size,
               batch_size=128, dataset='CelebA', num_workers=1):
    """Build and return a data loader."""
    transform = []
    if mode == 'train':
        transform = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
        ])


    if dataset == 'CelebA':
        dataset = CelebA(image_dir, resize_size, transform)
    else:
        print('specified dataset not present')
        return None

    data_loader = data.DataLoader(dataset=dataset,
                                  batch_size=batch_size,
                                  shuffle=True,
                                  num_workers=num_workers)
    return data_loader
