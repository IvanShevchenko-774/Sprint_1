class Tester:
    def __init__(self, name, deadline=True):
        self.name = name
        self.deadline = deadline

    def work_hard(self, deadline=None):
        # если при вызове метода передали параметр, обновим его
        if deadline is not None:
            self.deadline = deadline

        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')


tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # tester_1 Можно отдыхать

tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # tester_2 Что ж, ещё часок поработаю!