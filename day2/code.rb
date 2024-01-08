LIMITS = {
  :red => 12,
  :green => 13,
  :blue => 14
}

def game_scenario(games, style)
  for game in games do
    game_num, game_hands = game.split(': ')
    game_hands = game_hands.split('; ')
    puts(game_hands)
  end
end

def read_file(path)
  f = File.read(path)
  return f.split('\n')
end

file_contents = read_file('./day2/test.txt')
game_scenario(file_contents, true)
