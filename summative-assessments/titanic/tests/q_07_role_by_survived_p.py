test = {
  'name': 'Question 07_role_by_survived_p',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'role_by_survived_p'
          >>> 'role_by_survived_p' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'role_by_survived_p'
          >>> # from its initial state (of ...)
          >>> role_by_survived_p is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The values in the table should be proportions
          >>> # and sum to around 1 across the rows.
          >>> np.allclose(role_by_survived_p.transpose().sum(), 1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> isinstance(role_by_survived_p, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> role_by_survived_p.shape
          (8, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(role_by_survived_p) == ['no', 'yes']
          True
          >>> list(role_by_survived_p.T) == [
          ...         '1st',
          ...         '2nd',
          ...         '3rd',
          ...         'catering',
          ...         'deck',
          ...         'engineering',
          ...         'guarantee',
          ...         'musician']
          True
          >>> np.allclose(role_by_survived_p, [
          ...        [0.649718, 0.350282],
          ...        [0.853659, 0.146341],
          ...        [0.847870, 0.152130],
          ...        [0.838574, 0.161426],
          ...        [0.348485, 0.651515],
          ...        [0.780864, 0.219136],
          ...        [1.000000, 0.000000],
          ...        [1.000000, 0.000000]])
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
