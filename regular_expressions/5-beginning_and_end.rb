#!/usr/bin/env ruby

# Ensure exactly one argument is provided
if ARGV.length != 1
  puts "Usage: ruby match_hn.rb <string>"
  exit
end

# Take the first argument
input = ARGV[0]

# Regular expression: string starts with h, ends with n, one char in between
regex = /^h.n$/

# Pass the argument to the regex matching method
if input =~ regex
  puts "Matched: '#{input}' fits the pattern h?n"
else
  puts "No match: '#{input}' does not fit the pattern h?n"
end
