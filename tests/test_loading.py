# import unittest
# import time
# import nationstates as ns

# USERAGENT = "Automated Testing Builds by Travis CL for the nationstates API wrapper by Dolphman"

# class TestApi(object):

#     __rltime__ = []

#     @property
#     def xrls(self):
#         return 0



"""
#world = nationstates.Nationstates(
#    "world", shard=["numnations"], api_mother=TestApi()).load(USERAGENT)

nationstates = ns.nationstates(USERAGENT)
wa = nationstates.wa("0")
nation = nationstates.nation("testlandia")
region = nationstates.region("Balder")

"""
"""
These Test Makes sure that data accesses is consistant. (and that it can be accessed)
"""
"""

class NationTest(unittest.TestCase):

    def test_nation(self):
        for x in nation.collect().keys():
            self.assertEqual(nation[x], getattr(nation, x))

    def test_repr(self):
        self.assertIsInstance(nation.__repr__(), str)


class RegionTest(unittest.TestCase):

    def test_nation(self):
        for x in region.collect().keys():
            self.assertEqual(region[x], getattr(region, x))

    def test_repr(self):
        self.assertIsInstance(region.__repr__(), str)


class WorldTest(unittest.TestCase):

    def test_world(self):
        for x in world.collect().keys():
            self.assertEqual(world[x], getattr(world, x))

    def test_repr(self):
        self.assertIsInstance(world.__repr__(), str)

    def test_numnations(self):
        self.assertTrue(bool(world.numnations)) 


class WaTest(unittest.TestCase):

    def test_world(self):
        for x in world.collect().keys():
            self.assertEqual(wa[x], getattr(wa, x))

    def test_repr(self):
        self.assertIsInstance(wa.__repr__(), str)


class TestUserAgent(unittest.TestCase):

    def test_nation_user_agent(self):
        self.assertEqual(USERAGENT, nation.data["request_instance"].request.headers["User-Agent"])

    def test_region_user_agent(self):
        self.assertEqual(USERAGENT, region.data["request_instance"].request.headers["User-Agent"])

    def test_world_user_agent(self):
        self.assertEqual(USERAGENT, world.data["request_instance"].request.headers["User-Agent"])

    def test_wa_user_agent(self):
        self.assertEqual(USERAGENT, wa.data["request_instance"].request.headers["User-Agent"])
"""