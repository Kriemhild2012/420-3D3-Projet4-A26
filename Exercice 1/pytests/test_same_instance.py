from journal import Journal

def test_deux_journal_meme_instance():
	j1 = Journal()
	j2 = Journal()

	assert (j1 is j2)

def test_message_entre_deux_instances():
	j1 = Journal()
	j2 = Journal()

	j1.enregistrer(f"Validation de messages 1 !!!")

	assert j1.nb_messages() == j2.nb_messages()
	assert j1.afficher() == j2.afficher()
