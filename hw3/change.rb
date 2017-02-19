require 'net-telnet'

conn = Net::Telnet::new("Host" => "104.236.253.250",
                        "Port" => "31337")

conn.waitfor("String" => "$") { |s| puts s.split("\n")[0] }
conn.waitfor("String" => "$") { |s| puts s }
