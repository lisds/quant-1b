test = {
  'name': 'Question 04_publications',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'publications'
          >>> 'publications' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'publications'
          >>> # from its initial state (of ...)
          >>> publications is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Publication counts should be between 0 and 4
          >>> publications = np.asarray(publications)
          >>> np.all(publications >= 0)
          True
          >>> np.all(publications <= 4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        # In [27]: res = np.random.binomial(17, 0.9, size=(10000, 4, 10000))
        # In [30]: counts = np.count_nonzero(res == 17, axis=1)
        # In [34]: means = np.mean(counts, axis=1)
        # In [35]: np.min(means), np.max(means)
        # (0.641, 0.6952)
        # In [36]: stds = np.std(counts, axis=1)
        # In [37]: np.min(stds), np.max(stds)
        # (0.7244509576223915, 0.7676897745834577)
        {
          'code': r"""
          >>> 0.64 <= np.mean(publications) <= 0.70
          True
          >>> 0.72 <= np.std(publications) <= 0.77
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
