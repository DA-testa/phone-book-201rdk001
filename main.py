# python3

class ContactList:
    def __init__(self, bucket_capacity):
        self._prime = 231
        self._multiplier = 10
        self.bucket_capacity = bucket_capacity
        self.buckets = [ [] for i in range(bucket_capacity) ]

    def  _hash(self, num):
        hash = 0

        while num > 0:
            hash = (hash * self._multiplier + (num & 0b1111)) % self._prime
            num = num >> 4

        return hash % self.bucket_capacity

    def add(self, query):
        bucket = self.buckets[self._hash(query.number)]

        for contact in bucket:
            if contact.number == query.number:
                contact.name = query.name
                break
        else:
            bucket.append(query)

    def delete(self, query):
        bucket = self.buckets[self._hash(query.number)]

        for j in range(len(bucket)):
            if bucket[j].number == query.number:
                bucket.pop(j)
                break

    def find(self, query):
        for contact in self.buckets[self._hash(query.number)]:
            if contact.number == query.number:
                return contact.name

        return 'not found'


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = ContactList(10)
    
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts.add(cur_query)
        elif cur_query.type == 'del':
            contacts.delete(cur_query)
        else:
            result.append(contacts.find(cur_query))

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

