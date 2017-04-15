import math
def batches(batch_size, features, labels):
    """
    Create batches of features and labels
    :param batch_size: The batch size
    :param features: List of features
    :param labels: List of labels
    :return: Batches of (Features, Labels)
    """
    assert len(features) == len(labels)
    # TODO: Implement batching
    num_batch = math.ceil(len(features) / float(batch_size))
    batches = []
    for i in range(num_batch):
        batch = []
        feature_batch = []
        label_batch = []
        for j in range(batch_size):
            index = i * batch_size + j
            if index >= len(features):
                break

            feature_batch.append(features[index])
            label_batch.append(labels[index])
        batch.append(feature_batch)
        batch.append(label_batch)
        batches.append(batch)

    return batches