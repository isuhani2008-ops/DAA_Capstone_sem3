"""Merge Sort implementation for parcel prioritization."""


def parcel_sort_key(parcel):
    """Earlier deadline first; for ties, higher priority first."""
    return (parcel["deadline"], -parcel["priority"], parcel["id"])


def merge_sort_parcels(parcels):
    """Return a new list sorted using Merge Sort. Original list is unchanged."""
    if len(parcels) <= 1:
        return parcels[:]

    middle = len(parcels) // 2
    left = merge_sort_parcels(parcels[:middle])
    right = merge_sort_parcels(parcels[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if parcel_sort_key(left[i]) <= parcel_sort_key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
