#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to a pointer to the first node in the list
 * Return: a 0 if it is not a palindrome and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int llen, i, llen2;
	listint_t *tmp, *comp, *new, *compcpy;

	for (llen = 0, tmp = *head; tmp; llen++, tmp = tmp->next)
		;
	llen2 = ((llen / 2) - 1);
	comp = NULL;
	for (i = 0, tmp = *head; i <= llen2; i++, tmp = tmp->next)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (98);
		new->n = tmp->n;
		new->next = NULL;
		if (comp == NULL)
			comp = new;
		else
		{
			new->next = comp;
			comp = new;
		}
	}
	if (llen % 2 != 0)
		tmp = tmp->next;
	compcpy = comp;
	while (comp)
	{
		if (comp->n != tmp->n)
		{
			free_listint(compcpy);
			return (0);
		}
		comp = comp->next;
		tmp = tmp->next;
	}
	free_listint(compcpy);
	return (1);
}
