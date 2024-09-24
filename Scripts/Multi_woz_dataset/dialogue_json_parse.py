import json
import csv

def split_text_into_chunks(text):
    chunks = []
    words = text.split()
    current_chunk = []
    current_length = 0

    for word in words:
        if word.endswith(('.', '?', '!')):
            current_chunk.append(word)
            current_length += 1  # Add 1 for the space
            if current_length > 100:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_length = 0
        else:
            current_chunk.append(word)
            current_length += 1

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


with open('csv/knowledgebase.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'text'])

# Open the JSONL file
with open('csv/multi_woz_dataset-train.jsonl', 'r') as f:
    # Process each line separately
    for line in f:
        data = json.loads(line)  # Parse JSON from each line
        turns = data['turns']
        dialogue_id = data['dialogue_id'].split(".")[0]
        print(dialogue_id)
        
        #generate category
        active_intents = set()
        for frame in turns['frames']:
            if 'state' in frame:
                for state in frame['state']:
                    active_intent = state.get('active_intent')
                    if active_intent:
                        active_intents.add(active_intent)
        category = dialogue_id +'_' + '_'.join(active_intents)

        # generate whole conversation with speaker 
        conversations = ''
        for i, utter in enumerate(turns['utterance']):
            # print(utter)
            if i % 2 == 0:
                conversations += "User: " + utter + '\n'
            else:
                conversations += "Assistant: " + utter + '\n'

        # print(conversations)
        with open('csv/conversation.txt', 'a') as txtfile:
            txtfile.write(dialogue_id + "\n")
            txtfile.write(conversations + "\n\n")

        chunks = split_text_into_chunks(conversations)

        with open('csv/knowledgebase.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for chunk in chunks:
                writer.writerow([category, chunk])
