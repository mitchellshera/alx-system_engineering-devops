#!/usr/bin/env ruby

log_file = 'text_document.log'  # Path to the log file

File.foreach(log_file) do |line|
  match_data = line.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]
    puts "#{sender},#{receiver},#{flags}"
  end
end
