#!/usr/bin/env ruby

input = ARGV[0]  # Get the argument passed to the script

matches = input.scan(/School/)  # Find all occurrences of "School" in the input

result = matches.join('')  # Join the matching results

puts result
