import datetime
import urllib.request
import boto3

def watch(url):
    cloudwatch = boto3.client('cloudwatch')
    started_at = datetime.datetime.now()
    with urllib.request.urlopen("https://example.com"):
        ended_at = datetime.datetime.now()
        elapsed = (ended_at - started_at).total_seconds()
        cloudwatch.put_metric_data(
            Namespace='Watcher',
            MetricData=[{
                'MetricName': 'ResponseTime',
                'Unit': 'Milliseconds',
                'Value': elapsed,
                'Dimensions': [
                    {'Name': 'URL', 'Value': 'https://example.com'}
                ]
            }]
        )
        print(elapsed)

if __name__ == '__main__':
    import sys
    watch(sys.argv[1])
