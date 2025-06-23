test = {
  'name': 'Question 05_p_at_least_one',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_at_least_one'
          >>> 'p_at_least_one' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_at_least_one'
          >>> # from its initial state (of ...)
          >>> p_at_least_one is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Proportion should be between 0 and 1
          >>> 0 <= p_at_least_one <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        # In [27]: res = np.random.binomial(17, 0.9, size=(10000, 4, 10000))
        # In [30]: counts = np.count_nonzero(res == 17, axis=1)
        # In [38]: ps = np.count_nonzero(counts, axis=1) / counts.shape[1]
        # In [39]: np.min(ps), np.max(ps)
        # Out[39]: (0.494, 0.537)
        {
          'code': r"""
          >>> 0.49 <= p_at_least_one <= 0.54
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
