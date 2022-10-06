from godwin_assignment.Heart_rate_test import MaxiHeart

if __name__ == '__main__':
    myHeart = MaxiHeart(45)
    print(f'the patient age is {myHeart.get_age()}')
    print(f'heart rate is {myHeart.get_maximum_heart_rate()}')
    print(f'target heart rate is {myHeart.get_target_heart_rate()}')

