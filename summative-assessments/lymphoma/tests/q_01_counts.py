test = {
  'name': 'Question 01_counts',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'counts'
          >>> 'counts' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'counts'
          >>> # from its initial state (of ...)
          >>> counts is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Counts should all be from 0 through 17.
          >>> _my_counts = np.asarray(counts)
          >>> np.all(_my_counts >= 0)
          True
          >>> np.all(_my_counts <= 17)
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          # [ins] In [11]: res = np.random.binomial(17, 0.9, size=(10000, 10000))
          # [ins] In [12]: means = np.mean(res, axis=1)
          # Out[13]: array([15.2616999, 15.3373003])
          # [ins] In [14]: np.min(means), np.max(means)
          # Out[14]: (15.253, 15.3475)
          # [ins] In [15]: stds = np.std(res, axis=1)
          # [ins] In [16]: np.min(stds), np.max(stds)
          # Out[16]: (1.1995277028897666, 1.2749177855846237)
          'code': r"""
          >>> 15.25 <= np.mean(counts) <= 15.35
          True
          >>> 1.19 <= np.std(counts) <= 1.28
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
