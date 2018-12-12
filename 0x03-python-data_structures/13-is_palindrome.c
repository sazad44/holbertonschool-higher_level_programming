#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to a pointer to the first node in the list
 * Return: a 0 if it is not a palindrome and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int llen, i, llen2, j;
	listint_t *tmp, *tmp1;

	for (llen = 0, tmp = *head; tmp; llen++, tmp = tmp->next)
		;
	llen2 = llen;
	for (i = 0, tmp = *head; i < llen/2; i++, tmp = tmp->next, llen2--)
	{
		for (tmp1 = *head, j = 0; j < llen2 - 1; j++, tmp1 = tmp1->next)
			;
		if (tmp1->n != tmp->n)
			return (0);
	}
	return (1);
}
