#!/usr/bin/env ruby

# Ensure exactly one argument is provided
if ARGV.length != 1
  puts "Usage: ruby phone_match.rb <10-digit-number>"
  exit
end

# Take the first argument
input = ARGV[0]

# Regular expression: exactly 10 digits
regex = /^\d{10}$/

# Pass the argument to the regex matching method
if input =~ regex
  puts "Matched: '#{input}' is a valid 10-digit phone number"
else
  puts "No match: '#{input}' is not a valid 10-digit phone number"
end
