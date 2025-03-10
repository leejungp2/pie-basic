#Skeleton Code


import random

class Character:

  def __init__(self, speed):
    self.speed = speed


class Item:

  def __init__(self, item_type, speed_change):
    self.item_type = item_type
    self.speed_change = speed_change


class Player:

  def __init__(self, name):
    self.name = name # 플레이어의 이름 저장
    self.speed = 0 # 플레이어의 속도: 선택한 character의 속도!
    self.round_speed = 0 # 아이템 적용 후 플레이어의 속도
    self.play_records = [] # 플레이어의 경기 기록: 라운드별 주행 시간[초]


  def add_play_record(self, record_in_hr):
    """
    - 플레이어의 경기 기록을 받아 저장합니다.
    - 시간 단위로 들어온 기록을 초 단위의 기록으로 변환해 저장해야합니다. 
    - Game 클래스의 play_round() 함수에서 호출됩니다. 
    """
    # TODO : 플레이어의 경기 기록을 초 단위로 변환해 저장해주세요.
    from self.play_records
    import self.play_records
    import times
    print('00:00:00,000', '%I:%M:%S')

class Game:

  def __init__(self):
    self.num_rounds = 3
    self.player_list = [] # 플레이어의 목록. 이후에 set_players를 이용해 수정
    self.item_list = [] # 아이템의 목록. 이후에 set_item_list를 이용해 수정
    self.character_list = []


  def set_players(self):
    """
    - 5명의 플레이어를 생성하는 함수입니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    """

    # TODO :
    player1 =  Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()
    player5 = Player()
    
    
    #플레이어 목록(self.player_list)에 추가해주세요. 



  def start_game(self):
    """
    - 게임 규칙의 [게임 시작 전] 부분을 담당하는 함수입니다. 
    - 3 종류의 캐릭터와 2 종류의 아이템을 초기화하고, 사용자의 입력을 받아 각 플레이어의 속도를 설정합니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    """

    # TODO (1): 범위 내의 속도를 가진 세 종류의 캐릭터를 생성해주세요. 
    


    # TODO (2): 사용자의 입력을 받아 플레이어의 고유 속도를 설정하고, 선택된 캐릭터의 속도를 출력해주세요. 

    
    # TODO (3): 두 종류의 아이템을 생성해 아이템 목록(self.item_list)에 추가해주세요.
    


  def play_round(self):
    """
    - 게임 규칙의 [라운드 시작 전], [라운드 진행], [라운드 종료 후] 부분을 담당하는 함수입니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    """

    #### [라운드 시작 전]
    # TODO (1) - 1: 트랙의 길이를 결정해 변수에 저장하고, 출력해주세요. 
    for i in range(5,30):

      print('')


    # TODO (1) - 2: 5명의 플레이어에게 아이템을 랜덤하게 적용시키고, 적용된 아이템과 적용 후 플레이어의 속도를 출력해주세요. 

        
    #### [라운드 진행] , [라운드 종료 후]
    # TODO (2) : 플레이어가 트랙을 도는 데 걸린 시간을 초 단위로 출력하고, 플레이어의 경기 기록에 추가해주세요. Player 클래스의 함수를 사용해야합니다.  
    

  def game_result(self):
    """
    - 게임 규칙의 [게임 종료 후] 부분을 담당하는 함수입니다. 
    - 1, 2, 3순위까지 플레이어의 이름과 합산기록을 출력합니다. 
    - 동일 클래스의 game()에서 호출됩니다. 
    - 파이썬의 sorted() 함수와 sort() 함수를 잘 이용하시면 편합니다. sorting key 등을 검색해보시기를 추천합니다. 
    """
    # TODO : 사용자를 합산 기록 순으로 정렬하고, 상위 3명의 경기 기록 합산을 출력합니다. 
    

  def game(self):
    """
    - 게임 운영을 위한 함수입니다. 
    - 별도의 코드 작성이 필요 없습니다. 
    """
    self.set_players()
    self.start_game()

    print("******************* 게임 시작 *******************")
    for i in range(3):
      print(f"============= ROUND {i+1} =============")
      self.play_round()
      print()
    print()

    print("******************* 명예의 전당 *******************")
    self.game_result()
    



if __name__ == '__main__':
  """
    - 코드를 실행하는 부분입니다. 
    - 역시 별도의 코드 작성이 필요 없습니다. 
    """
  game = Game()
  game.game()