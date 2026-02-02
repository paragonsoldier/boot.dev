def args_logger(*args, **kwargs):
  count = 0
  for arg in args:
    count += 1
    print(f"{count}. {arg}")
  
  keywords = sorted(kwargs)
  for key in keywords:
    print(f"* {key}: {kwargs[key]}")

