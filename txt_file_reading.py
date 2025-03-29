# 'r' -> read-only, assumed if left out

file_for_reading = open('reading_file.txt', 'r')
file_for_reading2 = open('reading_file.txt')

# 'w' -> write -- will destroy the file if it already exists

file_for_writing = open('writing_file.txt', 'w')

# 'a' -> append -- for adding to the end of the file

file_for_appending = open('appending_file.txt', 'a')

# close files when done

file_for_writing.close()