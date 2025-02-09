test = {
  'name': 'Question 06_fake_mean_diffs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'fake_mean_diffs'
          >>> 'fake_mean_diffs' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'fake_mean_diffs'
          >>> # from its initial state (of ...)
          >>> fake_mean_diffs is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(fake_mean_diffs)
          10000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.mean(fake_mean_diffs), 1) == 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>>  -0.0063 <= np.mean(fake_mean_diffs) <= 0.0063
          True
          >>>  0.15 <= np.std(fake_mean_diffs) <= 0.16
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
