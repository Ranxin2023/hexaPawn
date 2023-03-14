import unittest
import osakaplayer
class osakatest(unittest.TestCase):
    def test_zero_txt(self):
        state=['----','-w-','bw','-b-','----']
        my_best_white=osakaplayer.osakaplayer(state, 'w',2)
        all_best_white_states=[['----','-w-','b-','-bw','----'],
                               ['----','---','-w','wb-','----'],
                               ['----','-w-','b-','---','-w--']]
        self.assertTrue(my_best_white in all_best_white_states)
        my_best_black=osakaplayer.osakaplayer(state, 'b',2)
        all_best_black_states=[['--b-','---','-w','-b-','----'],
                               ['----','bw-','-w','-b-','----'],
                               ['----','-wb','b-','---','----']]
        self.assertTrue(my_best_black in all_best_black_states)

    def test_one_txt(self):
        state=['w-ww','---','w-','b--','b-bb']
        my_best_white=osakaplayer.osakaplayer(state, 'w',2)
        all_best_white_states=[['--ww','w--','w-','b--','b-bb'],
                               ['w--w','-w-','w-','b--','b-bb'],
                               ['w--w','--w','w-','b--','b-bb'],
                               ['w-w-','--w','w-','b--','b-bb'],
                               ['w-ww','---','--','bw-','b-bb']]
        self.assertTrue(my_best_white in all_best_white_states)
        my_best_black=osakaplayer.osakaplayer(state, 'b',2)
        all_best_black_states=[['w-ww','---','--','---','b-bb'],
                               ['w-ww','---','w-','bb-','b--b'],
                               ['w-ww','---','w-','b-b','b--b'],
                               ['w-ww','---','w-','b-b','b-b-']]
        self.assertTrue(my_best_black in all_best_black_states)

    def test_two_txt(self):
        state=['-b---','wwww','bbb','w-','---','----','-----']
        my_best_white=osakaplayer.osakaplayer(state, 'w',3)
        all_best_white_states=[['-b---','w-ww','b-b','ww','---','----','-----'],
                               ['-b---','www-','bb-','ww','---','----','-----'],
                               ['-b---','wwww','bbb','--','-w-','----','-----'],
                               ['-b---','wwww','bbb','--','w--','----','-----']]
        self.assertTrue(my_best_white in all_best_white_states)
        my_best_black=osakaplayer.osakaplayer(state, 'b', 3)
        all_best_black_states=[['-bb--','w-ww','-bb','w-','---','----','-----'],
                               ['bb---','-www','-bb','w-','---','----','-----'],
                               ['-b-b-','ww-w','b-b','w-','---','----','-----'],
                               ['-b--b','www-','bb-','w-','---','----','-----']]
        self.assertTrue(my_best_black in all_best_black_states)
    def test_five_txt(self):
        state=['--b----','---w--','--w--','-b--','ww-','bw','-b-','----','-----','------','-w-----']
        my_best_white=osakaplayer.osakaplayer(state, 'w',2)
        all_best_white_states=[['--b----','------','--ww-','-b--','ww-','bw','-b-','----','-----','------','-w-----'],
                               ['--b----','---w--','-----','-bw-','ww-','bw','-b-','----','-----','------','-w-----'],
                               ['--b----','---w--','--w--','-b--','w--','-w','wb-','----','-----','------','-w-----'],
                               ['--b----','---w--','--w--','-b--','ww-','b-','-bw','----','-----','------','-w-----'],
                               ['--b----','---w--','--w--','-b--','ww-','b-','---','-w--','-----','------','-w-----']]
        self.assertTrue(my_best_white in all_best_white_states)

if __name__=='__main__':
    unittest.main()
