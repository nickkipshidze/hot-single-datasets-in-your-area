import fetchsets
import datasetvalue
import prettyout

datasets = fetchsets.get_datasets(count=50, dataframe=False)
ranked = sorted(datasets, key=datasetvalue.opportunity_score, reverse=True)

prettyout.pretty_datasets_output(
    ranked
)