#!/usr/bin/env ruby

# Ensure the user provides one argument
if ARGV.length != 1
  puts "Usage: ruby match_school.rb <string>"
  exit
end

# Take the first argument
input = ARGV[0]

# Regular expression to match "School"
regex = /School/

# Check if the input matches
if input =~ regex
  puts "Matched: '#{input}' contains 'School'"
else
  puts "No match: '#{input}' does not contain 'School'"
end
