#!/usr/bin/env ruby

# Ensure exactly one argument is provided
if ARGV.length != 1
  puts "Usage: ruby match_school.rb <string>"
  exit
end

# Take the first argument
input = ARGV[0]

# Regular expression: whole word "School", case-insensitive
regex = /\bSchool\b/i

# Pass the argument to the regex matching method
if input =~ regex
  puts "Matched: '#{input}' contains the word 'School'"
else
  puts "No match: '#{input}' does not contain the word 'School'"
end
