import textract
import yaml

def main():
    print(extractSkills())

def extractSkills():
    text = textExtractUtf8("test.pdf")
    text = text.lower()
    text = text.split('\n')
    config = loadConfig()
    searchParams = config['extractors']
    awsParams = searchParams['AWS']
    awsTags = searchParams['AWS_tags']
    resumeSkills = []
    print(awsParams)
    for line in text:
        for tag in awsTags:
            if tag in line:
                resumeSkills.append(tag)
        for key, tags in awsParams.items():
            key = key.lower()
            if key in line and key not in resumeSkills:
                resumeSkills = resumeSkills + tags
    resumeSkills = set(resumeSkills)
    return resumeSkills

def loadConfig():
    with open('config.yaml', 'r') as f:
        config = yaml.load(f)
    return config

def textExtractUtf8(f):
    try:
        text = textract.process(f)
        return text.decode("utf-8")
    except UnicodeDecodeError:
        return

if __name__ == '__main__':
    main()