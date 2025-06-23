test = {
  'name': 'Question 02_p_100',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_100'
          >>> 'p_100' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_100'
          >>> # from its initial state (of ...)
          >>> p_100 is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Proportion should be between 0 and 1
          >>> 0 <= p_100 <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          # [ins] In [11]: res = np.random.binomial(17, 0.9, size=(10000, 10000))
          # [ins] In [19]: ps = np.count_nonzero(res == 17, axis=1) / 10000
          # [ins] In [20]: np.min(ps), np.max(ps)
          # Out[20]: (0.1536, 0.1804)
          'code': r"""
          >>> # Proportion should be between 0 and 1
          >>> 0.152 <= p_100 <= 0.181
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: end-extra
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
