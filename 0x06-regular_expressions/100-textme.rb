#!/usr/bin/env ruby

log_file = ARGV[0]  # Get the log file path passed to the script

results = []

File.foreach(log_file) do |line|
  if line =~ /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
    sender = $1
    receiver = $2
    flags = $3
    results << "#{sender},#{receiver},#{flags}"
  end
end

puts results.join("\n")
