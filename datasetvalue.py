import fetchsets

def opportunity_score(dataset):
    downloads, kernels, views, votes, usability = dataset[2:]

    if kernels > 1:
        return 0

    attention = (views + 10) * (votes + 0.5) * downloads
    score = attention * usability
    return score

if __name__ == "__main__":
    datasets = fetchsets.get_datasets(count=5, dataframe=False)
    ranked = sorted(datasets, key=opportunity_score, reverse=True)

    print(*ranked, sep="\n")