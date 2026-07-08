from CH08L04_queue import Queue


def matchmake(queue: Queue, user: tuple[str, str]) -> str:
    if user[1] == "leave":
        queue.search_and_remove(user[0])
    
    if user[1] == "join":
        queue.push(user[0])
    
    if queue.size() >= 4:
        return f"{queue.pop()} matched {queue.pop()}!"
    
    return "No match found"

