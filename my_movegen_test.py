import unittest
import movegen
class test_movegen(unittest.TestCase):
    def test_first_case(self):
        state=['w-ww', '---', 'w-', 'b--', 'b-bb']
        next_states_w=[['--ww', 'w--', 'w-', 'b--', 'b-bb'],
                     ['w--w', '-w-', 'w-', 'b--', 'b-bb'],
                     ['w--w', '--w', 'w-', 'b--', 'b-bb'],
                     ['w-w-', '--w', 'w-', 'b--', 'b-bb'],
                     ['w-ww', '---', '--', 'bw-', 'b-bb']]
        next_states_b=[['w-ww', '-b-', '--', '---', 'b-bb'],
                       ['w-ww', '---', 'w-', 'bb-', 'b--b'],
                       ['w-ww', '---', 'w-', 'b-b', 'b--b'],
                       ['w-ww', '---', 'w-', 'b-b', 'b-b-']]
        
        my_next_states_b=movegen.movegen(state, 'b')
        my_next_states_w=movegen.movegen(state, 'w')
        for my_next_state in my_next_states_b:
            if my_next_state not in next_states_b:
                self.assertTrue(False)
        self.assertEqual(len(my_next_states_b), len(next_states_b))
        for my_next_state in my_next_states_w:
            if my_next_state not in next_states_w:
                self.assertTrue(False)
        self.assertEqual(len(my_next_states_w), len(next_states_w))

    def test_second_case(self):
        state=['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----']
        next_states_w=[['-------', '-bb---', '----b', 'wwb-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['-------', '-bb---', '--w-b', '--b-', 'w-b', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '---', '--b-', '--w-w', '---w--', '-w-----'],
                       ['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '---', '--b-', '--ww-', '---w--', '-w-----'],
                       ['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '-----', '--ww--', '-w-----'],
                       ['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '--w--', '------', '-w--w--'],
                       ['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '--w--', '------', '-w-w---']]
        next_states_b=[['--b----', '--b---', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['-b-----', '--b---', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['---b---', '-b----', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['--b----', '-b----', '--w-b', 'w-b-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['-------', '-bb--b', '--w--', 'w-b-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['-------', '-bb-b-', '--w--', 'w-b-', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['-------', '-bb---', '--wbb', 'w---', '--b', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['-------', '-bb---', '--w-b', 'w-bb', '---', '--', '---', '--bw', '--w--', '---w--', '-w-----'],
                       ['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '-b-', '---w', '--w--', '---w--', '-w-----'],
                       ['-------', '-bb---', '--w-b', 'w-b-', '--b', '--', '--b', '---w', '--w--', '---w--', '-w-----']]
        my_next_states_w=movegen.movegen(state,'w')
        for my_next_state in my_next_states_w:
            if my_next_state not in next_states_w:
                self.assertTrue(False)
        self.assertEqual(len(my_next_states_w),len(next_states_w))
        my_next_states_b=movegen.movegen(state,'b')
        for my_next_state in my_next_states_b:
            if my_next_state not in next_states_b:
                self.assertTrue(False)
        self.assertEqual(len(my_next_states_b),len(next_states_b))

    def test_third_case(self):
        state=['-b---', 'wwww', 'bbb', 'w-', '---', '----', '-----']
        next_states_w=[['-b---', 'w-ww', 'b-b', 'ww', '---', '----', '-----'], ['-b---', 'www-', 'bb-', 'ww', '---', '----', '-----'],
                       ['-b---', 'wwww', 'bbb', '--', '-w-', '----', '-----'], ['-b---', 'wwww', 'bbb', '--', 'w--', '----', '-----']]
        next_states_b=[['-bb--', 'w-ww', '-bb', 'w-', '---', '----', '-----'], ['bb---', '-www', '-bb', 'w-', '---', '----', '-----'],
                       ['-b-b-', 'ww-w', 'b-b', 'w-', '---', '----', '-----'], ['-b--b', 'www-', 'bb-', 'w-', '---', '----', '-----'],
                       ['-bb--', 'ww-w', 'bb-', 'w-', '---', '----', '-----']]             
        my_next_states_w=movegen.movegen(state,'w')
        for my_next_state in my_next_states_w:
            if my_next_state not in next_states_w:
                self.assertTrue(False)
        self.assertEqual(len(my_next_states_w),len(next_states_w))
        my_next_states_b=movegen.movegen(state,'b')
        for my_next_state in my_next_states_b:
            if my_next_state not in next_states_b:
                self.assertTrue(False)
        self.assertEqual(len(my_next_states_b),len(next_states_b))

    def test_fourth_case(self):
        state =  ['-----', '----', '---', 'b-', 'www', 'bbbb', '-w---']
        next_states_w = [['-----', '----', '---', 'b-', '-ww', 'b-bb', '-ww--'], ['-----', '----', '---', 'b-', '-ww', '-bbb', 'ww---'],
                  ['-----', '----', '---', 'b-', 'w-w', 'bb-b', '-w-w-'], ['-----', '----', '---', 'b-', 'ww-', 'bbb-', '-w--w'],
                         ['-----', '----', '---', 'b-', 'ww-', 'bb-b', '-ww--']]
        next_states_b = [['-----', '----', '-b-', '--', 'www', 'bbbb', '-w---'], ['-----', '----', 'b--', '--', 'www', 'bbbb', '-w---'],
                        ['-----', '----', '---', 'bb', 'w-w', 'b-bb', '-w---'], ['-----', '----', '---', 'bb', 'ww-', 'bbb-', '-w---']]
        my_next_states_w=movegen.movegen(state,'w')
        for my_next_state in my_next_states_w:
            if my_next_state not in next_states_w:
                self.assertTrue(False)
        self.assertEqual(len(my_next_states_w),len(next_states_w))
        my_next_states_b=movegen.movegen(state,'b')
        for my_next_state in my_next_states_b:
            if my_next_state not in next_states_b:
                self.assertTrue(False)
        self.assertEqual(len(my_next_states_b),len(next_states_b))

if __name__=='__main__':
    unittest.main()
