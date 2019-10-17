    def test_for_each(self):
        arr = []
        def cb(x): return arr.append(x)

        v1 = random.randint(1, 101)
        v2 = random.randint(1, 101)
        v3 = random.randint(1, 101)
        v4 = random.randint(1, 101)
        v5 = random.randint(1, 101)

        self.bst.insert(v1)
        self.bst.insert(v2)
        self.bst.insert(v3)
        self.bst.insert(v4)
        self.bst.insert(v5)

        self.bst.for_each(cb)

        self.assertTrue(5 in arr)
        self.assertTrue(v1 in arr)
        self.assertTrue(v2 in arr)
        self.assertTrue(v3 in arr)
        self.assertTrue(v4 in arr)
        self.assertTrue(v5 in arr)