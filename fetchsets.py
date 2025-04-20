import kaggle
import kaggle.cli
import pandas as pd

def get_datasets_page(**kwargs):
    datasets_raw = kaggle.cli.api.dataset_list(**kwargs)
    datasets = []

    for dataset in datasets_raw:
        datasets.append([
            dataset.ref,
            dataset.url,
            dataset.download_count,
            dataset.kernel_count,
            dataset.view_count,
            dataset.vote_count,
            dataset.usability_rating
        ])
    
    return datasets

def get_datasets(count=20, dataframe=True):
    datasets = []
    page = 1

    while len(datasets) < count:
        datasets += get_datasets_page(sort_by="updated", page=page)
        page += 1
    
    datasets = datasets[:count]

    if dataframe:
        dataframe = pd.DataFrame(
            data=datasets,
            columns=[
                "ref",
                "url",
                "download_count",
                "kernel_count",
                "view_count",
                "vote_count",
                "usability_rating"
            ]
        )
    
        return dataframe
    else:
        return datasets

if __name__ == "__main__":
    dsts = get_datasets(count=50, dataframe=False)
    refs = [d[0] for d in dsts]

    print(
        len(refs), len(set(refs))
    )