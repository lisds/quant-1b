test = {
  'name': 'Question 2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < us_birth_rate < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> np.isclose(us_birth_rate, 0.012358536498646102)
          True
          """,
          'hidden': False,
          'locked': False
        }
        #: end-extra
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
