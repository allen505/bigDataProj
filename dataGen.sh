#!/bin/zsh

# Check if a numeric argument is provided
if ! [[ "$1" =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 <number of times to run the command>"
  exit 1
fi

# Store the number of times to run the command in a variable
n=$1
video_id=$2
# Run the curl command n times
for ((i=1; i<=n; i++))
do
  curl 'http://127.0.0.1:5000/ana/mark_opened' \
    -H 'Accept: */*' \
    -H 'Accept-Language: en-US,en;q=0.9' \
    -H 'Connection: keep-alive' \
    -H 'Content-Type: application/json' \
    -H 'Cookie: session=eyJlbWFpbCI6ImFsbGVuQSIsInVzZXJuYW1lIjoiQWxsZW4gQWJyYWhhbSJ9.Zj1Ixw.aEQdHe-W4e200b26agXW556McpE; username-127-0-0-1-3888="2|1:0|10:1715292512|23:username-127-0-0-1-3888|192:eyJ1c2VybmFtZSI6ICI1Yjg4OGE5YjYzNmM0ZjVmOWQzYzhhOTRmMzU1MWFmMSIsICJuYW1lIjogIkFub255bW91cyBUaGViZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIFRoZWJlIiwgImluaXRpYWxzIjogIkFUIiwgImNvbG9yIjogbnVsbH0=|42c289455ee0215b4c4910e925d36f47a4e72a9a051eed6a24f3293669e1825a"' \
    -H 'DNT: 1' \
    -H 'Origin: http://127.0.0.1:5000' \
    -H 'Referer: http://127.0.0.1:5000/home' \
    -H 'Sec-Fetch-Dest: empty' \
    -H 'Sec-Fetch-Mode: cors' \
    -H 'Sec-Fetch-Site: same-origin' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' \
    -H 'X-Requested-With: XMLHttpRequest' \
    -H 'sec-ch-ua: "Not-A.Brand";v="99", "Chromium";v="124"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "macOS"' \
    --data-raw '{"video_id":"video_id"}'
  echo ""
done

echo "\nCompleted sending $n requests."
