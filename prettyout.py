def pretty_datasets_output(datasets):
    for index, dataset in reversed(list(enumerate(datasets, 1))):
        ref, url, downloads, kernels, views, votes, usability = dataset
        
        print(
            f"# {index:0>3} - {ref}",
            f" . . Downloads : {downloads}",
            f" . . Kernels   : {kernels}",
            f" . . Views     : {views}",
            f" . . Upvotes   : {votes}",
            f" . . Usability : {usability:.2f}",
            sep="\n",
            end="\n\n"
        )
