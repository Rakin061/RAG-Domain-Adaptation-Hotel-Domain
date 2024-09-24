from datasets import load_dataset

from datasets import load_from_disk

raw_datasets = load_dataset("multi_woz_v22")
raw_datasets.cache_files

raw_datasets.save_to_disk("multi_woz-arrow-datasets")


arrow_datasets_reloaded = load_from_disk("multi_woz-arrow-datasets")
arrow_datasets_reloaded

for split, dataset in raw_datasets.items():
    dataset.to_csv(f"multi_woz_dataset-{split}.csv", index=None)


for split, dataset in raw_datasets.items():
    dataset.to_json(f"multi_woz_dataset-{split}.jsonl")