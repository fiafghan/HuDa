import chardet

def detect_encoding(file_path, sample_size=50000):
    """Detect the text encoding of a file."""
    with open(file_path, 'rb') as f:
        rawdata = f.read(sample_size)
    result = chardet.detect(rawdata)
    return result['encoding']
