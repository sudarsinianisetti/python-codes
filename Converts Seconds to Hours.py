seconds = int(input())
hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
secs = remaining % 60
print("H:M:S-{}:{}:{}".format(hours,minutes,secs))
