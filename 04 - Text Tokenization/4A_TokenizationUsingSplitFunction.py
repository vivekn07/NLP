# Define the text variable with a multi-line string
text = """ This tool is in a beta stage. Electric cars are running petrol cars raw and rough experience. It also supports custom battery model, prebuilt charging model, and the Autonomous Driving API. You can use this tool for creation of monitors, alarms, and dashboards that spotlight changes. The release of these three tools will enable developers to create visual rich experiences for Electric cars with advanced infotainment systems. Electric car manufacturers describe these tools as the collection of tech and tools for creating visually rich and interactive driving experiences."""

# Split the text into sentences using the period as a delimiter
data = text.split('.')

# Iterate over each sentence in the list
for i in data:
    # Print each sentence after stripping leading and trailing whitespace
    print(i.strip())
