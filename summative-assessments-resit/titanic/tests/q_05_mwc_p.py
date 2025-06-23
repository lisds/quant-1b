test = {
  'name': 'Question 05_mwc_p',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'mwc_by_survived_p'
          >>> 'mwc_by_survived_p' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'mwc_by_survived_p'
          >>> # from its initial state (of ...)
          >>> mwc_by_survived_p is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(mwc_by_survived_p, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> mwc_by_survived_p.shape
          (3, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The values in the table should be proportions
          >>> # and sum to around 1 across the rows.
          >>> np.allclose(mwc_by_survived_p.transpose().sum(), 1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> list(mwc_by_survived_p) == ['no', 'yes']
          True
          >>> list(mwc_by_survived_p.T) == ['child', 'female', 'male']
          True
          >>> np.allclose(mwc_by_survived_p, [[0.475806, 0.524194],
          ...                                 [0.243056, 0.756944],
          ...                                 [0.806784, 0.193216]])
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
