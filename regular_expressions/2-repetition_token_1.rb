#!/usr/bin/env ruby

# Ensure exactly one argument is provided
if ARGV.length != 1
  puts "Usage: ruby parse_message.rb '<log_entry>'"
  exit
end

input = ARGV[0]

# Regular expressions
sender_regex   = /from:(\+?\d{10,}|[A-Za-z]+)/i
receiver_regex = /to:(\+?\d{10,}|[A-Za-z]+)/i
flags_regex    = /flags:(\S+)/i

# Extract values
sender   = input.match(sender_regex)&.captures&.first || "UNKNOWN"
receiver = input.match(receiver_regex)&.captures&.first || "UNKNOWN"
flags    = input.match(flags_regex)&.captures&.first || "NONE"

# Output in required format
puts "[#{sender}],[#{receiver}],[#{flags}]"
