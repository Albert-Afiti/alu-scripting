#!/usr/bin/env ruby

# Ensure exactly one argument is provided
if ARGV.length != 1
  puts "Usage: ruby match_caps.rb <string>"
  exit
end

# Take the first argument
input = ARGV[0]

# Regular expression: only capital letters
regex = /^[A-Z]+$/

# Pass the argument to the regex matching method
if input =~ regex
  puts "Matched: '#{input}' contains only capital letters"
else
  puts "No match: '#{input}' does not contain only capital letters"
end
