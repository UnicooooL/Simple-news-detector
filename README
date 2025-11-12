## Testing Results

Deployed website:

http://serve-sentiment-env.eba-fkss5nn8.us-east-2.elasticbeanstalk.com/demo

### Functional Test
| Input | Prediction |
|--------|-------------|
| Breaking: the president has resigned amid scandal | FAKE |
| NASA successfully launches new satellite to study Mars | FAKE |
| Celebrity claims drinking bleach cures disease | FAKE |
| Stock market reaches record high after strong earnings | REAL |

![Function Test Result](functional_result.png)

### Latency Test

I performed latency testing on the deployed AWS Elastic Beanstalk Flask API.  
Each of the four test cases was sent 100 POST requests to the `/predict` endpoint.

![Latency Boxplot](latency_boxplot_with_avg.png)

**Results summary:**
- Average latency: ~80 ms   
- Performance consistent across all four test cases  

Overall, the deployed API demonstrates **stable and low-latency** responses suitable for lightweight ML inference workloads.

