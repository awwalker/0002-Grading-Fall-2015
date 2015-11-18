import unittest
from translate_passage import translate



class Tester(unittest.TestCase):

	def test_translator(self):
		text = """I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight."""
		self.maxDiff = None
		self.assertEqual(translate(text),"""i amway alreadyway arfay orthnay ofway ondonlay, andway asway i alkway inway ethay treetssay ofway etersburghpay, i eelfay a oldcay orthernnay reezebay laypay uponway ymay eekschay, hichway racesbay ymay ervesnay andway illsfay emay ithway elightday.""")



if __name__ == '__main__':
	unittest.main()
	